#!/usr/bin/python
#****************************************************************************
#
# PRO : Copernicus Marine
# MOD : graph_cascade.py
# ROL : Generate the adcp graph
#
# CRE : 11/12/2022
# AUT : TC
# VER : $Revision$
#       $Date$
#
#****************************************************************************
# 
# HST : 12/03/2020	TC 	Creation
#		23/01/2022	TC 	suppression des lignes vides de courant
#
#****************************************************************************
#
# Credit, Ifremer, 2022
#
#****************************************************************************	
import time
import os
import sys
import s3fs
import xarray as xr
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
import cmocean
import matplotlib.colors as clr
import matplotlib.dates as mdates
import numpy as np
from os.path import basename
from optparse import OptionParser
from numpy import arange

# Enregistrer l'index
# def save_index(png0, param0):
# 	FileName0 = png0 + '.txt'
# 	fna0 = os.path.splitext(basename(png0))[0] + '.png'
# 	dir0 = fna0.split('_')
# 	cod0 = dir0[3]
# 	dir0 = dir0[0] + '_' + dir0[1] + '_' + dir0[2] + '_' + dir0[3] + '/'
# 	reg0 = pid0.split('_')[0]
# 	typ0 = pid0.split('_')[1] + '_' + pid0.split('_')[2]
# 	idx0 = htt0 + '/' + dir0 + fna0 + ',' + cod0 + ',' + nam0 + ',' + reg0 + ',' + typ0 + ',' + param0 + '\n'

# 	if0 = open(FileName0, 'w')
# 	if0.write(idx0)
# 	if0.close

# Initialisation des graphiques
def init_graphique(ds0, title0, param0):

	# Initialisation du graphique
	copyright0 = u'\N{COPYRIGHT SIGN}'.lower()
	info0 = 'file:' + fin0 + ', ' + copyright0 + 'coriolis ' + time.strftime('%Y-%m-%d')

	plt.figure(figsize=(16,9))
	plt.rc('font', size=10)          # controls default text sizes
	plt.title(title0)
	plt.figtext(0.05, 0.95, info0, horizontalalignment='left', verticalalignment='center')

	# Palette de couleur
	if param0 == 'TEMP':
		cmap0 = 'cmo.thermal'
	elif param0 == 'PSAL':
		cmap0 = 'cmo.haline'
	elif param0 == 'CHLA':
		cmap0 = 'cmo.algae'
	elif param0 == 'CDOM':
		cmap0 = 'cmo.matter'
	elif param0 == 'BBP700':
		cmap0 = 'cmo.solar'
	else:
		cmap0 = 'jet'

	return plt, cmap0


# Tracer le paramètre
def plot_param(ds0, png0, param0):

	title0 = 'Trajectory of float ' + nam0 + ': ' + param0
	if 'standard_name' in ds0[param0].attrs:
		title0 = title0 + ' - ' + ds0[param0].standard_name
	(plt, cmap0) = init_graphique(ds0, title0, param0)
	pointseries = plt.gca() 
	pointseries.set_xlabel('time')

	pointseries.set_ylabel('PRES' + ' (' + ds0['PRES'].units + ')')

	v0 = np.array(ds0[param0])[~np.isnan(ds0[param0])]
	print(param0)
	print(v0)
	if (len(v0) > 0):
		MinP1 = np.percentile(v0, 10)
		MaxP1 = np.percentile(v0, 90)
		MiniP1 = np.min(v0)
		MaxiP1 = np.max(v0)

		scatter0 = pointseries.scatter(ds0['JULD'], ds0['PRES'], c=ds0[param0], cmap = cmap0, vmin = MinP1, vmax = MaxP1, s=2)
		pointseries.invert_yaxis()
		colorbar = plt.colorbar(scatter0)
		colorbar.set_label(param0 + ' (' + ds0[param0].units + ') - min:' + str(MiniP1) + ' - max:' + str(MaxiP1))

		plt.savefig(png0)
		# plt.show()
	else:
		print('Empty parameter: ' + param0)

	plt.close()

	# save_index(GraphFile1, 'cur')

# Plot each parameters
def plot_parameters(ds0, Dest0, fin0):

	# Iterate on parameters
	for v0 in ds0.variables:
		if v0 in ['TEMP', 'PSAL', 'DOXY', 'CHLA', 'CDOM', 'BBP700', 'PH_IN_SITU_TOTAL', 'NITRATE']:
#		if v0 in ['TEMP', 'PSAL']:
			v0_qc = v0 + '_QC'
			png0 = Dest0 + '/' + fin0 + '-' + v0 + '.png'
			ds1 = xr.merge( [\
				ds0['JULD'], \
				ds0['JULD_QC'], \
				ds0[v0], \
				ds0[v0_qc], \
				ds0['PRES'], \
				ds0['PRES_QC'] \
				])
			# ds2 = ds1.where((ds1['JULD_QC'] == b'1') & (ds1[v0_qc] == b'1'))
			ds2 = ds1.where((ds1['JULD_QC'] == b'1') & (ds1[v0_qc] != b'4'))

			plot_param(ds2, png0, v0)
			
			ds2.close()
			ds1.close()

# Main function
if __name__ == "__main__":
    # Read arguments
	parser = OptionParser("usage: %prog SourceFileName GraphFolder")
	(options, args) = parser.parse_args()
	if len(args) != 2:
		parser.error("incorrect number of arguments: FileName GraphFolder")
	else:
		FileName0 = args[0]
		GraphFolder0 = args[1]
	fin0 = os.path.splitext(basename(FileName0))[0]

	# Créer un système de fichiers S3 avec s3fs
	# s3 = s3fs.S3FileSystem(anon=False, key='AKIA6MMCO5ST7RSN2LXF', secret='*')
	s3 = s3fs.S3FileSystem(anon=True)

	# Ouvrir le fichier à partir de S3 en utilisant xarray
	print(FileName0)
	with s3.open(FileName0, 'rb') as s3_file:
	    ds0 = xr.open_dataset(s3_file)

	# Métadonnées principales
	# htt0 = 'https://co.ifremer.fr/co/graphics/argo-traj-' + param0 + '.png'
	nam0 = ds0['PLATFORM_NUMBER'].values
	nam0 = str(nam0.astype(str)).strip()
	pid0 = fin0

	# Initiate the file graph directory
	Dest0 = GraphFolder0 + '/' + nam0
	print(Dest0)
	if not os.path.exists(Dest0):
		os.makedirs(Dest0)

	plot_parameters(ds0, Dest0, fin0)

	ds0.close()
