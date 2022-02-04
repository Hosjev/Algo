SELECT e.name, e.salary
AS Employee
FROM Employee e
JOIN Employee e2 on e.managerId = e2.id
WHERE e.salary > e2.salary;
