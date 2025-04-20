# Databricks notebook source
dbutils.widgets.text("logic_app_url", "")
logic_app_url = dbutils.widgets.get("logic_app_url")

dbutils.widgets.text("email_id", "")
email_id = dbutils.widgets.get("email_id")

dbutils.widgets.text("storage_account", "")
storage_account = dbutils.widgets.get("storage_account")

dbutils.widgets.text("adls_url", "")
adls_url = dbutils.widgets.get("adls_url")

dbutils.widgets.text("gcp_bucket","")
gcp_bucket = dbutils.widgets.get("gcp_bucket")

dbutils.widgets.text("gcp_bucket","")
gcp_bucket = dbutils.widgets.get("gcp_bucket")

# COMMAND ----------

spark.sql(f"""         
insert into metadata_schema.tbl_source_control values 
('{gcp_bucket}','{storage_account}','{adls_url}','landing','{logic_app_url}','{email_id}')        
""")

# COMMAND ----------

spark.sql("""
insert into metadata_schema.tbl_parameters values 
(201,'telecom/dim_cities','2001-01-01T15:13:23.963Z','dev_raw','dim_cities','dev_intermediate','dim_cities',NULL,NULL,NULL,NULL),
(202,'telecom/dim_date','2001-01-01T15:13:23.963Z','dev_raw','dim_date','dev_intermediate','dim_date',NULL,NULL,NULL,NULL),
(203,'telecom/dim_plan','2001-01-01T15:13:23.963Z','dev_raw','dim_plan','dev_intermediate','dim_plan',NULL,NULL,NULL,NULL),
(204,'telecom/fact_company','2001-01-01T15:13:23.963Z','dev_raw','fact_metrics_share','dev_intermediate','fact_metrics_share',NULL,NULL,NULL,NULL),
(205,'telecom/fact_market','2001-01-01T15:13:23.963Z','dev_raw','fact_market_share','dev_intermediate','fact_market_share',NULL,NULL,NULL,NULL),
(206,'telecom/fact_plan','2001-01-01T15:13:23.963Z','dev_raw','fact_plan_revenue','dev_intermediate','fact_plan_revenue',NULL,NULL,NULL,NULL)
""")
