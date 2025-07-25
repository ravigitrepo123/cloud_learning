

- [Databricks Architecture](#databricks-architecture)
- [Types of Clusters in Azure databricks](#types-of-clusters-in-azure-databricks)
- [How are Azure dbx notebooks saved and deployed in real world](#how-are-azure-databrick-notebooks-are-saved-and-deployed-in-real-world)
- [ How is ADLS gen2 is integrated and used in ADB](#how-is-adls-gen2-is-integrated-and-used-in-adb)
- [ CI/CD for ADB, migration from Dev to Test and PROD]()
- [How do you call ADB notebks in ADF]()
- [How do you call a notebook from another notebook](#how-do-you-call-a-notebook-from-another-notebook)
- [How to address performance issues in ADBx]()
- [sample ADB project structure]()
## Databricks Architecture 
Databricks operates out of a control plane and a data plane.

https://learn.microsoft.com/en-us/azure/databricks/getting-started/overview

The **control plane** includes the backend services that Azure Databricks manages in its own Azure account. 
**Notebook** commands and many other **workspace configurations** are stored in the control plane and encrypted at rest.

Your Azure account manages the **data plane**,(compute plane new terminology) and is where your **actual data resides**. This is also where data is processed exampple **ADLS Gen2**. Use Azure Databricks connectors to connect clusters to external data sources outside of your Azure account to ingest data, or for storage. You can also ingest data from external streaming data sources, such as events data, streaming data, IoT data, and more.

## Types of Clusters in Azure databricks

General purpose clusters/Interactive Cluster:
All developers can interact with this cluster generally used in development environments

Job cluster :
Cluster is accessible only when a job is started and terminates after job is ended.generally used in prod

Memory optimized for not ETL/ELT process
Storage Optimized clusters for Shuffle intensive work

## How do you call a notebook from another notebook
run dbutils.notebook.run calls another notebook with timelimit to run and paramters

child_notebook

dbutils.widgets.text("param1", "")
param1 = dbutils.widgets.get("param1")

Do some logic with param1...
dbutils.notebook.exit("Processed in Environment: " + param1)

parent notebook 

....

result = dbutils.notebook.**run**("/Users/ravi/child_notebook", 60, {"param1": "Dev"})

...

## How are Azure databrick notebooks are saved and deployed in real world


##  How is ADLS gen2 is integrated and used in ADB
In production Best approach is using Service Principal 

In Dev Create Mount points (eg: /mount/adlsgen2_test) using ADLS acccess key , which points to ADLS gen2 containeter. as it is easy to use shortcut paths

https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/Azure%20Databricks/Learning/Resources/ADLS%20Integration%20with%20Databricks.docx



