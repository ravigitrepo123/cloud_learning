# Azure Data Engineering Project Plan

---

## Sprint-1: Resource Creation for Dev (Infra Setup)

- **[15 min]** User Story 1: Creating resource groups or environments in Azure  
  [Resource Group Guide](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)

- **[45 min]** User Story 2: Creating Azure resources
  - Task 1: Create VNet and two subnets (Private + Public) for ADB VNet ingestion
  - Task 2: Create Azure Databricks workspace + cluster
  - Task 3: Create Azure Data Factory
  - Task 4: Configure Azure Git Version Control
  - Task 5: Create Storage account (ADLS Gen2)
  - Task 6: Create Azure Key Vault
  - Task 7: Create Logic App

  Resources:
  - [ADLS Gen2 Creation](https://learn.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account)
  - [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory)
  - [Databricks Workspace](https://learn.microsoft.com/en-us/azure/databricks/getting-started/)
  - [Key vault creation](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal)
  - [Logic App creation](https://learn.microsoft.com/en-us/azure/logic-apps/quickstart-create-example-consumption-workflow)

- **[45 min]** User Story 3: Creating Containers
- (landing,raw,intermediate,curated,metadata,log,archive) inside ADLS gen2 Storage account
---

## Sprint-2: Establishing the Connectivity (Infra Setup)

- **[10 min]** Intro: Integration Runtime, Linked Services, Dataset
- **[15 min]** User Story 1: Create self-hosted SHIR in ADF
- **[30 min]** User Story 2: Creating linked services for:
  - Task 1: Key Vault  ls_azure_keyVault
  - Task 2: ADLS Gen2   ls_adls
  - Task 3: ADB  ls_databricks_compute , ls_databricks_delta_lake

- **[20 min]** User Story 3: Create linked services for GCP cloud storage ls_gcp
- **[10 min]** User Story 4: Create secrets for GCP linked service in Azure Key Vault
- **[15 min]** User Story 5: Create SPN for ADB-ADLS connectivity
- **[15 min]** User Story 6: Set up Spark Configuration for cluster
- **[10 min]** User Story 7: Create Secret scope

---

## Sprint-3: GCP Source Data Ingestion

- **[15 min]** Sprint review discussion
- **[10 min]** User Story 1: Setting up input data source (Upload datasets into GCP bucket)
- **[30 min]** User Story 2: Create datasets in ADF
  - Task 1: [ds_input_gcp] GCP input dataset (Source)
  - Task 2: [ds_output_csv] CSV output dataset
  - Task 3: [ds_metadata_adb_deltalake] ADB Delta Lake input dataset for metadata lookup

- **[10 min]** User Story 3: Create folder structure in Databricks,setting up input metadata, log tables in databricks hive_metastore by running the notebooks

   Add image to dbricks folder
  
   [Create hivemetastore db, dev_raw schema, log_record_tbl table](https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/cleverstudies_adf_db_uc_rbac_proj_2/set_up/table_creation/log_table_creation_scripts.py)

   [create metadata_schema in hivemetastore db , tbl_source_control , tbl_parameters in that schema](https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/cleverstudies_adf_db_uc_rbac_proj_2/set_up/table_creation/metadata_tables_creation_scripts.py)

   [Insert data in metadata_schema.tbl_source_control , metadata_schema.tbl_parameters](https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/cleverstudies_adf_db_uc_rbac_proj_2/set_up/table_insertion/metadata_tables_insert_scripts_till_raw.py)
   
  
- **[30 min]** User Story 4: Create ADF pipeline (GCP to Landing), with logging , parameterization

**Checks:**
- File availability
- File name (Telecom)
- File format / extension (.csv)

ADF Pipeline:
- `1a_pl_dim_gcp_to_azure_full_load`
- 
Databricks notebook py scripts called

[Water column update after copy success ](https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/cleverstudies_adf_db_uc_rbac_proj_2/databricks_notebooks/dbx_update_watermark_column.py)

[called at failures and success to log into log table](https://github.com/ravigitrepo123/cloud_learning/blob/main/Azure/cleverstudies_adf_db_uc_rbac_proj_2/databricks_notebooks/log_record_tbl_insert.py)

---

## Sprint-4: Data Enrichment & Transformation using Databricks

- **[30 min]** User Story 1: Create ADF pipeline (GCP to Landing) with logging and parameterization

**Checks:**
- File availability
- File name (Telecom)
- File format / extension (.csv)

Links:
- `2a_pl_fact_gcp_to_azure_delta_load`

- **[15 min]** User Story 2:
  - Task 1: Import raw table scripts from notebooks
  - Task 2: Create tables in raw schema

- **[20 min]** Cleaning Activities:
  - Bad Records Handling | Permissive
  - Adding Derived columns: load_id, last_inserted_dttm_azure, last_updated_dttm_gcp
  - Remove nulls  at record level
  - Duplicate checks
    
- **[30 min]** User Story 3: Create ADF pipeline (Landing to Raw) [Full Load]
  - `1b_pl_dim_sub_landing_to_raw_full_load`

- **[30 min]** User Story 4: Create ADF pipeline (Landing to Raw) [Delta Load]
  - `2b_pl_sub_fact_landing_to_raw_delta_load`
---

## Sprint-5: Develop Business Logic with Archiving, Logging

- **[15 min]** Sprint review
- **[20 min]** User Story 1: Archive source files after raw layer ingestion
- **[15 min]** Cleaning Activities:
  - Merge or Upsert
  - Incremental Load
  - Full Load

- **[10 min]** User Story 2:
  - Task 1: Import intermediate table scripts(Databricks noteboks)
  - Task 2: Create tables in intermediate schema by running scripts of task1

- **[30 min]** User Story 3: Create ADF pipeline (Raw to Intermediate) with logging , paramterization.
  - `1c_pl_dim_raw_to_intermediate`

- **[30 min]** User Story 4: Create ADF pipeline (Raw to Intermediate)  with logging , paramterization
- `2c_pl_fact_raw_to_intermediate`

---

## Sprint-6: Triggers, Alerts, Unit Testing

- **[10 min]** Sprint Review

**Implement Business Logic:**
- Joins
- Merge
- CTE

- **[30 min]** User Story 1: Create ADF pipeline (Intermediate to Curated) with logging , paramterization
  - `3_pl_intermediate_to_curated`

- **[20 min]** User Story 2: Configure Logic App for email alerts
- **[30 min]** Email Alerting (4 templates)
  - Template 1: Count mismatch email alert
  - Template 2: ADF PL in progress email alert
  - Template 3: ADF PL error email alert
  - Template 4: ADF PL completion email alert

- **[15 min]** User Story 3: Create triggers, run ADF pipeline via loop
- **[15 min]** User Story 4: Unit testing and end-to-end ADF PL execution through triggers

---

## Sprint-7: RBAC and Unity Catalog

- **[15 min]** Sprint-6 Review
- **[10 min]** Intro to RBAC

### User Story 1: Create AAD Groups in Entra ID
- Task 1: Add users to AAD groups

### User Story 2: Create SCIM Connector App
- Task 1: Add AAD groups to SCIM connector
- Task 2: Verify provisioning

### User Story 3: Add AAD groups to Databricks workspace
### User Story 4: Assign roles to AAD groups

- **[15 min]** Intro to Unity Catalog

### User Story 5: Create schemas in Unity Catalog
### User Story 6: Create storage credentials
- Task 1: Access connector
- Task 2: External credentials
- Task 3: External locations

### User Story 7: Sync Hive metastore schemas to Unity Catalog
### User Story 8: Grant UC & cluster permissions to AAD groups


---

## Sprint-8: RBAC UC Pipeline & Prod Deployment

- **[10 min]** Sprint-7 Review
- **User Story 1:** ADF PL for RBAC and UC
- **User Story 2:** Databricks table lineage
- **User Story 3:** Triggers
- **[20 min]** User Story 4: Create prod env (resource groups, etc.)
- **[20 min]** User Story 5: Create SHIR for prod
- **[20 min]** User Story 6: Create and execute DevOps ADO pipeline for Databricks

---

## Sprint-9: Q&A and Backlogs

- **[10 min]** Sprint Review
- **[30 min]** User Story 1: Create and execute DevOps ADO pipeline for ADF
- **[15 min]** Project Call Sheet
- **[30 min]** Project Q&A

