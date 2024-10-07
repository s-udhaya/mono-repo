# Databricks notebook source
# MAGIC %run ./add_project_to_sys_path


# COMMAND ----------

from inference import inference

##############################################################################################
#                             Databricks Widgets Creation
##############################################################################################
dbutils.widgets.text("env", "dev", "environment")
dbutils.widgets.text("input_table_name", "features", "name of the input delta table")
dbutils.widgets.text("experiment_name", "/shared/", "mlflow experiment path")
dbutils.widgets.text("model_name", "clv", "mflflow model name")



# COMMAND ----------

##############################################################################################
#                             Reading Widgets' Values
##############################################################################################
env = dbutils.widgets.get("env")
input_table_name = dbutils.widgets.get("input_table_name")
experiment_name = dbutils.widgets.get("experiment_name")
model_name = dbutils.widgets.get("model_name")


# COMMAND ----------

inference_params = {
    "env": env,
    "input_table_name": input_table_name,
    "model_name": model_name,
    "experiment_name": experiment_name,
}
print(inference_params)

# COMMAND ----------

inference.run_inference(inference_params)