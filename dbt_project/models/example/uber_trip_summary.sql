SELECT
    city,
    payment_method,
    COUNT(*) AS total_trips,
    AVG(fare_amount) AS average_fare,
    AVG(distance_km) AS average_distance
FROM read_csv_auto('../data/cleaned_dataset.csv')
GROUP BY city, payment_method