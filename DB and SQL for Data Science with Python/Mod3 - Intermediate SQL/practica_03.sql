# Retrieve the list of all employees, first and last names, whose first names start with ‘S’.

SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE F_NAME LIKE 'S%'

# Arrange all the records of the EMPLOYEES table in ascending order of the date of birth.
SELECT *
FROM EMPLOYEES
ORDER BY B_DATE ASC;

# Group the records in terms of the department IDs and filter them of ones that have average salary more than or equal to 60000. Display the department ID and the average salary.
SELECT DEP_ID, AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000;

# For the problem above, sort the results for each group in descending order of average salary.
SELECT DEP_ID, AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000
ORDER BY AVG_SALARY DESC;

# Write a query to find the average salary of the five least-earning employees.
SELECT AVG(SALARY) AS "AVG_SALARY_LEAST_5"
FROM (
    SELECT SALARY
    FROM EMPLOYEES
    ORDER BY SALARY ASC
    LIMIT 5
) AS LEAST_5;

# Write a query to find the records of employees older than the average age of all employees.
SELECT * 
FROM EMPLOYEES
WHERE B_DATE < (
    SELECT AVG(B_DATE)
    FROM EMPLOYEES
);

# From the Job_History table, display the list of Employee IDs, years of service, and average years of service for all entries.
SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))), 
    (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE)))) 
    FROM JOB_HISTORY)
FROM JOB_HISTORY;

# Retrieve only the list of employees whose JOB_TITLE is Jr. Designer.
# a. Using sub-queries

SELECT *
FROM EMPLOYEES
WHERE EMP_ID IN (
    SELECT EMP_ID
    FROM JOBS
    WHERE JOB_TITLE = 'Jr. Designer'
);

# b. Using Implicit Joins
SELECT E.*
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT
AND J.JOB_TITLE = 'Jr. Designer';

# Retrieve JOB information and a list of employees whose birth year is after 1976.
# a. Using sub-queries

SELECT *
FROM JOBS
WHERE JOB_IDENT IN (
    SELECT JOB_ID
    FROM EMPLOYEES
    WHERE YEAR(B_DATE) > 1976
);

# b. Using Implicit Joins
SELECT J.*  
FROM JOBS J, EMPLOYEES E
WHERE J.JOB_IDENT = E.JOB_ID
AND YEAR(E.B_DATE) > 1976