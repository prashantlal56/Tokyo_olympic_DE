## Tokyo Olympic

##### This project includes extracting data from Kaggal platform, executing an ETL pipeline using Microsoft Azure cloud services, conducting in-depth data analysis with Azure Synapse, and creating dashboards using Tableau


### Workflow :

![WorkFlow!](https://github.com/prashantlal56/Tokyo_olympic_DE/blob/main/Image/Screenshot%202024-03-03%20at%2000.10.58.png)

### Steps:
1. Extracting data from Kaggal
   Dataset source : [Kaggal](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo )
2. Creating data pipeline to store raw data in Azure Datalake Gen2 using Azure data factory cloud service
3. Scripting transformation query in Azure Databrick and storing the transformed data in Azure Datalake Gen2
4. Connecting the transformed data to Azure Synapse for data analysis
   For instance:
   * Total 11062 players participated in 46 different discipline from 206 different countries.
   * Amoung all players 23 players had participated in more than one discipline
   * Top 3 Female dominating discipline with female population percenatge:
      |Artistic Swimming    | 100%
      |Rhythmic Gymnastics  | 100%
      |Cycling BMX Freestyle| 52%
   * Top 3 Male dominating discipline with Male population percenatge:
      |Wrestling    | 66%
      |Cycling Road | 65%
      |Boxing       | 64%
6. Connecting with Tableau for data visualization
   
   ![Tableau](https://github.com/prashantlal56/Tokyo_olympic_DE/blob/main/Image/Screenshot%202024-03-02%20at%2022.12.49.png)
