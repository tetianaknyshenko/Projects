

# Создание набора данных BigQuery
resource "google_bigquery_dataset" "bg_ds" {
  dataset_id = "dstf"           # ID набора данных
  location   = "US"                        # Локация набора данных (например, US, EU и т.д.)

 # access {
 #   role          = "roles/TerraFormAdmin.dataOwner"
 #   user_by_email = "terraformadmin@terraformprojekt.iam.gserviceaccount.com"  # Предоставьте доступ нужным пользователям
 # }
}

# Создание таблицы BigQuery
resource "google_bigquery_table" "table_tf" {
  dataset_id = google_bigquery_dataset.bg_ds.dataset_id
  table_id   = "table_df"

  schema = jsonencode([
    {
      name = "id"
      type = "INTEGER"
      mode = "REQUIRED"
    },
    {
      name = "name"
      type = "STRING"
      mode = "NULLABLE"
    },
    {
      name = "age"
      type = "INTEGER"
      mode = "NULLABLE"
    }
  ])
  
  time_partitioning {
    type = "DAY"  # Добавляет разделение данных по дате
  }
}