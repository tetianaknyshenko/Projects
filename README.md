Data Analyst for Product Name Matching – Fuzzy Matching & Data Cleansing

We are looking for a data analyst or data scientist with experience in data cleansing, fuzzy matching, and text similarity analysis to compare and identify duplicate or near-duplicate products between two datasets. We have an excel file with fragrance product data on 12,000 products and we need the duplicates removed between the two sources below (CDPH & EWG)

🎯 Goal:

Compare CDPH (California Department of Public Health) dataset and EWG (Environmental Working Group) dataset
Identify and flag potential duplicate products based on product name similarity.
Provide an actionable report of matched products with a confidence score.

📂 Dataset Details:
The two datasets have different naming conventions and lack a unique identifier like UPC or Product ID.
CDPH dataset contains: Product Name, Brand, UPC, and Ingredient List.
EWG dataset contains: Product Name and Ingredients but no unique identifiers.
Challenge: Product names may differ (e.g., "Dove Body Wash" vs. "Dove Nourishing Body Cleanser").
🛠️ Expected Work Process:
Data Preprocessing

Clean and standardize product names (lowercase, remove extra spaces, punctuation, common words like “Eau de Parfum”).
Identify and remove unnecessary stopwords.
Fuzzy Matching / Similarity Analysis

Use fuzzy matching (Levenshtein Distance, Jaccard, Cosine Similarity, or other NLP techniques).
Implement TF-IDF and nearest neighbor search for optimized comparisons.
Use brand matching to enhance accuracy where available.
Flag possible duplicates with a confidence score.
Validation & Reporting

Deliver a final report (CSV, Excel, or Google Sheets) listing:
CDPH Product Name
EWG Matched Product Name
Match Confidence Score (0-100)
Include a summary of findings and any false positives observed.

📈 Expected Deliverables:
✅ Cleaned & Processed Dataset with standardized product names.
✅ Matched Product List with confidence scores.
✅ Python script or methodology documentation to replicate the process.
✅ Recommendations on improving future matching.
