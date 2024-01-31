# Write your MySQL query statement below
select x,y,z, case when x+y > z and x+z > y and y+z > x then 'Yes' else 'No' end as triangle from triangle

/* Intuition
The given SQL query determines whether a triangle can be formed based on the values of three sides (x, y, and z) from the "triangle" table. The query calculates the sum of two sides and compares it with the third side to check if the triangle inequality holds. The result is returned as 'Yes' if a triangle can be formed and 'No' otherwise.

Approach
The main query starts with the SELECT keyword followed by the column names x, y, z, and the CASE statement.
The CASE statement checks the condition x + y > z and x + z > y and y + z > x to determine if a triangle can be formed.
If the condition is true, the result is set to 'Yes'. Otherwise, it is set to 'No'.
The query retrieves the results from the "triangle" table.*/