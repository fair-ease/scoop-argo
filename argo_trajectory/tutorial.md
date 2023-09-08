---
layout: tutorial_hands_on

title: Argo trajectory
questions:
- Which biological questions are addressed by the tutorial?
- Which bioinformatics techniques are important to know for this type of data?
objectives:
- 
- 
- 
time_estimation: 1H
key_points:
- 
- 
- 
contributors:
- Marie59
---


# Introduction

The Earth and Environmental Dynamics study is a huge complex topic, according to the Earth system under analysis and the specific objectives under consideration. [FAIR-EASE](https://fairease.eu/) planned to include in this effort three different Pilots, each one focusing on different Earth systems, each one having specific goals to achieve.

![FAIR-EASE](../../images/biogeochemical/fair_ease_colour.png "Fair-Ease project logo")

This tutorial deals with the Bio-GeoChemical (BGC) Pilot. It focuses on marine environments, for which the knowledge of the BGC asset is fundamental to understand processes involving marine ecosystems, their dynamics and the impact on the health status of this precious Earth environment.
The observation of marine biogeochemical processes (BGC) is useful to address fundamental scientific questions regarding the health of marine ecosystems (e.g. ocean acidification, oxygen minimum zone, biological carbon pump, phytoplankton communities...) and needs for ocean resource management (e.g. Johnson et al., 2009; Chai et al., 2020). We count more than 910836 BGC profiles measured either by a BGC-Argo float, a glider or a sea-mammal throughout the World Ocean

Today, the BGC-Argo science team is the major contributor on an international initiative to calibrate, validate and trigger alerts on Ocean BGC in situ data. In recent years, BGC-Argo
sensors have diversified (oxygen, nitrate, chlorophyll, suspended particles, pH) and methods of data Quality Assessment and Control, validation and adjustment have become more complex. The aim here is to improve tools in support of data qualification/validation by expert teams, facilitating and harmonizing the data access and methodologies.

![ARGO](../../images/argo_logo.png "Argo progrem logo")
Argo is an international program that collects information from inside the ocean using a fleet of robotic instruments that drift with the ocean currents and move up and down between the surface and a mid-water level. Each instrument (float) spends almost all its life below the surface. [Learn more about Argo](https://argo.ucsd.edu/)

> <details-title>Earth sytsem definition</details-title>
> There are five main systems, or spheres, on Earth. The first one, the geosphere, consists of the interior and surface of Earth, both of which are made up of rocks. The limited part of the planet that can support living things comprises the second; these regions are referred to as the biosphere. In the third one are the areas of Earth that are covered with enormous amounts of water, called the hydrosphere. The atmosphere is the fourth, and it is an envelope of gas that keeps the planet warm and provides oxygen for breathing and carbon dioxide for photosynthesis. Finally, there is the fifth one, which contains huge quantities of ice at the poles and elsewhere, constituting the cryosphere. All five of these create the Earth system.
{: .details}

> <details-title>Specific data resources</details-title>
> As mentioned previously, the demonstrator will calibrate BGC sensors of in situ network/source Argo, Glider and sea-mammals. Aggregated in situ data set or products, model outputs, reanalysis and satellite products will be either used by method of calibration or for the data validation.
{: .details}


> <agenda-title></agenda-title>
>
> In this tutorial, we will cover:
>
> 1. TOC
> {:toc}
>
{: .agenda}

> <comment-title>This is best viewed in Pangeo Jupyter Lab</comment-title>
>
> 1. Create a history
>
>     > <hands-on-title>Create history</hands-on-title>
>     >
>     > 1. Make sure you start from an empty analysis history.
>     > 2. **Rename your history** to be meaningful and easy to find. For instance, you can choose **Argo trajectory notebook** as the name of your new history.
>     {: .hands_on}
>
>
> <comment-title>Upload S3 data</comment-title>
> >
> >   Data can be retrieved directly from [Registry of Open Data on AWS](https://registry.opendata.aws/argo-gdac-marinedata/).
> >   the next explanation are optionnal because we will directly download or data from the notebook. This is just to give some knowledge on the Galaxy options.
> >
> >   > <hands-on-title>Data upload</hands-on-title>
> >   >
> >   > 1. Create a new history for this tutorial
> >   > 2. Go on **User** on the top pannel. 
> >   > 3. Select Preferences, then **Manage Cloud Authorization** and click on **Create New Authorization Key**
> >   > 3. Write the Description, for instance "Argo Gdac"
> >   > 4. Copy paste in Role ARN the url, for instance "arn:aws:s3:::argo-gdac-sandbox"
> >   > 4. Click on **Save Key**
> >   >
> >   {: .hands_on}
> {: .comment}

> 2. Starting Galaxy Pangeo JupyterLab
>
>    > <hands-on-title>Launch Pangeo notebook JupyterLab in Galaxy</hands-on-title>
>    >
>    > Currently Pangeo notebook in Galaxy is available on [useGalaxy.eu](https://usegalaxy.eu) only. Make sure you login to Galaxy and search for Pangeo notebook and not the default JupyterLab in Galaxy to make sure you ahve all the Pangeo Software stack available. The default JupyterLab in Galaxy would not be sufficient for executing all the tasks in this tutorial.
>    >
>    > 1. Open the {% tool [Pangeo Notebook](interactive_tool_pangeo_notebook) %} by clicking [here to launch it on EU](https://usegalaxy.eu/?tool_id=interactive_tool_pangeo_notebook)
>    > 2. *Include data into the environment*: `CAMS-PM2_5-20211222.netcdf`
>    > 3. Click on **Run Tool**: the tool will start running and will stay running
>    > 4. Click on the **User** menu at the top and go to **Active Interactive Tools** and locate the Pangeo JupyterLab instance you started.
>    > 5. Click on your Pangeo JupyterLab instance
>    {: .hands_on}
>
> 4. Once the notebook has started, open a Terminal in Jupyter **File → New → Terminal**
>
> 5. Run the following command:
>
>    ```
>    wget {{ ipynbpath }}
>    ```
>
> 6. Switch to the Notebook that appears in the list of files on the left
{: .comment}

