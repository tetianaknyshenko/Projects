provider "google" {
  project     = "terraformprojekt"  # Укажите ваш Google Cloud Project ID
  region      = "us-central1"      # Укажите регион, если хотите
  credentials = file("terraformprojekt-c0e7b100c7bf.json")  # Путь к JSON-файлу с ключом
}