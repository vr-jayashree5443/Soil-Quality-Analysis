# Soil-Quality-Analysis
Here's a detailed description of the provided code:

1. **Import Libraries:**
   - Libraries such as `pandas` for data manipulation, `seaborn`, and `matplotlib.pyplot` for data visualization are imported.

2. **Load the Dataset:**
   - The code reads a CSV file containing soil analysis data using the `pd.read_csv` function.

3. **Calculate Soil Quality:**
   - A new column called 'Soil Quality' is created by summing up the values of pH Level, Organic Matter (%), Nitrogen Content (kg/ha), Phosphorus Content (kg/ha), and Potassium Content (kg/ha) for each row.

4. **Group Data:**
   - The dataset is grouped by 'District' and 'Soil Type' using the `groupby` function.

5. **Calculate Mean Soil Quality:**
   - The mean of all numeric columns for each group is calculated using the `mean()` function.

6. **Calculate Percentage of Soil Quality:**
   - The percentage of soil quality is calculated for each group, normalizing the 'Soil Quality' values.

7. **Sort Data by Percentage of Soil Quality:**
   - The data is sorted in descending order based on the calculated percentage of soil quality.

8. **Visualize Relationships:**
   - Bar plots are created to visualize the relationship between each variable (pH Level, Organic Matter (%), Nitrogen Content, Phosphorus Content, Potassium Content) and the percentage of soil quality. Each plot is displayed individually.
