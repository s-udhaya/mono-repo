# Databricks notebook source
import os
import sys


def add_notebook_path_to_sys_path():
    notebook_path = "/Workspace" + os.path.dirname(
        os.path.dirname(
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )
    )
    sys.path.append(notebook_path)


def add_project_files_path_to_sys_path():
    project_files_path = "/Workspace" + os.path.dirname(os.path.dirname(
        os.path.dirname(
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )
    )
    )
    sys.path.append(project_files_path)


# COMMAND ----------

add_notebook_path_to_sys_path()
add_project_files_path_to_sys_path()
