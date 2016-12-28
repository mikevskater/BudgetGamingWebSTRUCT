SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN psu AS B 
                        ON A.pcPart_id = B.psu_pcPart_id;