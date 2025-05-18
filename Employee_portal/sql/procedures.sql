-- Stored procedure to get all employee data
CREATE OR REPLACE FUNCTION get_all_employee_data()
RETURNS TABLE (
    name TEXT,
    role TEXT,
    location TEXT,
    years_of_experience NUMERIC,
    active BOOLEAN,
    current_comp NUMERIC,
    last_working_day DATE
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        name,
        role,
        location,
        years_of_experience,
        active,
        current_comp,
        last_working_day
    FROM employee_data;
END;
$$ LANGUAGE plpgsql;

-- Stored procedure to get all employee ratings
CREATE OR REPLACE FUNCTION get_all_employee_rating()
RETURNS TABLE (
    name TEXT,
    role TEXT,
    location TEXT,
    years_of_experience NUMERIC,
    l3q_self_rating NUMERIC,
    l3q_manager_rating NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        name,
        role,
        location,
        years_of_experience,
        l3q_self_rating,
        l3q_manager_rating
    FROM employee_rating;
END;
$$ LANGUAGE plpgsql;

-- Stored procedure to get all average industry compensation
CREATE OR REPLACE FUNCTION get_all_industry_compensation()
RETURNS TABLE (
    location TEXT,
    role TEXT,
    average_industry_compensation NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        location,
        role,
        average_industry_compensation
    FROM average_industry_compensation;
END;
$$ LANGUAGE plpgsql;


-- Stored procedure - Filter and Display Active Employees by Role
CREATE OR REPLACE FUNCTION get_filtered_employee_data(
    role_filter TEXT,
    include_inactive BOOLEAN,
    selected_location TEXT DEFAULT NULL
)
RETURNS TABLE (
    name TEXT,
    role TEXT,
    location TEXT,
    current_comp NUMERIC,
    avg_comp_for_location NUMERIC
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        e.name,
        e.role,
        e.location,
        e.current_comp,
        avg(e2.current_comp) FILTER (WHERE e2.location = e.location) OVER (PARTITION BY e.location) AS avg_comp_for_location
    FROM employee_data e
    JOIN employee_data e2 ON e2.location = e.location
    WHERE
        e.role = COALESCE(role_filter, e.role)
        AND (include_inactive OR e.active = TRUE)
        AND (selected_location IS NULL OR e.location = selected_location);
END;
$$ LANGUAGE plpgsql;
