# Databricks notebook source
# MAGIC %run ./add_project_to_sys_path

# COMMAND ----------

from validation import validator

##############################################################################################
#                             Databricks Widgets Creation
##############################################################################################
dbutils.widgets.text("env", "dev", "environment")
dbutils.widgets.text("experiment_name", "/shared/", "mlflow experiment path")
dbutils.widgets.text("model_name", "clv", "mflflow model name")
dbutils.widgets.text("run_mode", "dry_run", "run mode of validation step")

# COMMAND ----------

##############################################################################################
#                             Reading Widgets' Values
##############################################################################################
env = dbutils.widgets.get("env")
experiment_name = dbutils.widgets.get("experiment_name")
model_name = dbutils.widgets.get("model_name")
run_mode = dbutils.widgets.get("run_mode")


# COMMAND ----------

validation_params = {
    "env": env,
    "model_name": model_name,
    "experiment_name": experiment_name,
    "run_mode": run_mode
}
print(validation_params)

# COMMAND ----------

validator.run_validation(validation_params)