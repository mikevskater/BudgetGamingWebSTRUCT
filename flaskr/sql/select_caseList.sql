SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN cases AS B 
                        ON A.pcPart_id = B.case_pcPart_id;