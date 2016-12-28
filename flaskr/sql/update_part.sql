UPDATE pcPart
        SET
                pcPart_type = ?, 
                pcPart_name = ?,
                pcPart_modelNumber = ?,
                pcPart_price = ?,
                pcPart_desc = ?,
                pcPart_brand = ?,
                pcPart_condition = ?,
                pcPart_notes = ?,
                pcPart_test = ?,
                pcPart_age = ?
                        WHERE pcPart_id = ?