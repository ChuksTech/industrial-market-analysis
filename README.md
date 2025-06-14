# 🌍 Industrial Product Scraper & Market Analysis

This project scrapes and analyzes industrial product data from **Made-in-China.com**, focusing on categories like **Electronics**, **Agricultural Equipment**, and **Chemicals**. It helps uncover **economic signals** such as price distribution, manufacturer dominance, and product availability.

---

## 📦 Project Structure
industrial-scraping-project/
├── made_in_china_scraper # Selenium-based web scraper
├── data_cleaning script # Data cleaning and transformation scripts
├── Analysis_charts/ # EDA notebook and charts
├── cleaned_product_result # Raw and cleaned CSVs
├── product_results # Raw and cleaned CSVs
├── requirements.txt
└── README.md


---

## 🚀 How to Run This Project Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/industrial-scraping-project.git
cd industrial-scraping-project

##  Set Up Environment
pip install -r requirements.txt

## Scrape the Data
cd crawling
python made_in_china_scraper.py

## Clean & Transform the Data
cd ../industrial-scraping-project
python data_cleaning script.ipynb

## Run the Analysis
cd ../industrial-scraping-project
jupyter analysis_script.ipynb

🔍 Summary of Key Insights
1. 🧭 Price Distribution by Category and Product Type
Electronics: Wide price variation, indicating varying tech complexity.

Chemicals: Prices cluster within narrow bands, showing standardization.

Agricultural Equipment: Skewed price range due to high-end automation like drones.

### Price Distribution by Product Type and Category
![Price Distribution](Analysis_charts\Price_Distribution_by_Product_Type_and_Category.png)


2. 🏭 Top 10 Manufacturing Companies Overall

| Rank | Company Name                                          | Products |
| ---- | ----------------------------------------------------- | -------- |
| 1    | Veacam Electronics Co., Ltd                           | 101      |
| 2    | Zhejiang Sinray Electronics Co., Ltd                  | 76       |
| 3    | Kozen International Ltd                               | 56       |
| 4    | Smart Check Security Equipment (Shenzhen) Co., Ltd.   | 54       |
| 5    | Beijing TT Aviation Technology Co., Ltd.              | 52       |
| 6    | Zhuhai Jinwo Electronic Technology Co., Ltd           | 42       |
| 7    | Shandong Aolan Drone Science and Technology Co., Ltd. | 42       |
| 8    | Nanjing Essence Fine-Chemical Co., Ltd.               | 40       |
| 9    | Taizhou City Xiefeng Machinery Co., Ltd.              | 37       |
| 10   | Chongqing Yingka Electronic Co., Ltd.                 | 37       |

### Top 10 Manufacturing Companies
![Top 10 Companies](Analysis_charts\Top_10_Manufacturing_Companies_Overall.png)


3. 🧪 Top 5 Manufacturers by Category
🔌 Electronics
Veacam Electronics Co., Ltd

Zhejiang Sinray Electronics Co., Ltd

Kozen International Ltd

Smart Check Security Equipment (Shenzhen) Co., Ltd.

Zhuhai Jinwo Electronic Technology Co., Ltd

🧴 Chemicals
Nanjing Essence Fine-Chemical Co., Ltd

RUIGREAT CHEMICAL CO., LIMITED

Shanghai Bosman Industrial Co., Ltd

Greentree Chemical Co., LIMITED

Anhui Yier Agrochemical Co., Ltd

🚜 Agricultural Equipment
Beijing TT Aviation Technology Co., Ltd

Shandong Aolan Drone Science and Technology Co., Ltd

Taizhou City Xiefeng Machinery Co., Ltd

Nanjing Hongfei Aviation Technology Co., Ltd

Qingdao Hong Zhu Agricultural Machinery Co., Ltd

### Top 5 Manufacturers by Category
![Top 5 by Category](Analysis_charts\Top_5_Manufacturers_in_Each_Category.png)


💼 Economic Impact Takeaways
Market Dominance: Electronics sector is highly consolidated — the top 2 companies supply over 25% of listed products.

Affordability Signals: Price bands by product type reveal affordability trends and tech complexity.

Category Innovation: Drones and aviation tools in agri-tech signal growth in precision farming.

Sourcing Insight: Clear visibility of suppliers helps procurement decisions and industrial intelligence.

📋 Dependencies
Key libraries used:
selenium
beautifulsoup4
pandas
matplotlib
seaborn
(See full list in requirements.txt)

