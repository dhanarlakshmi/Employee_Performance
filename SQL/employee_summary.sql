-- Department Performance & Attrition Summary

SELECT
    e.Department,
    COUNT(DISTINCT e.Employee_ID) AS Total_Employees,
    ROUND(AVG(p.Performance_Rating), 2) AS Avg_Performance_Rating,
    ROUND(AVG(p.KPI_Score), 2) AS Avg_KPI_Score,
    ROUND(AVG(e.Tenure_Years), 1) AS Avg_Tenure,
    SUM(CASE WHEN a.Attrition_Flag = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(
        SUM(CASE WHEN a.Attrition_Flag = 'Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(DISTINCT e.Employee_ID), 2
    ) AS Attrition_Rate_Percentage
FROM Employee_Cleaned e
LEFT JOIN Performance_Cleaned p
    ON e.Employee_ID = p.Employee_ID
LEFT JOIN Attrition_Cleaned a
    ON e.Employee_ID = a.Employee_ID
GROUP BY e.Department
ORDER BY Attrition_Rate_Percentage DESC;
