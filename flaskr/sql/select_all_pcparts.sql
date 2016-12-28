SELECT
        pcPart_id,
        pcPart_type, 
        pcPart_name,
        pcPart_modelNumber,
        pcPart_price,
        pcPart_desc,
        pcPart_brand,
        pcPart_condition,
        pcPart_notes,
        pcPart_age
        FROM pcPart 
                ORDER BY pcPart_id 
                        DESC