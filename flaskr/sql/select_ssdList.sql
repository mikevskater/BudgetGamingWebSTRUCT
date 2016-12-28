SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN ssd AS B 
                        ON A.pcPart_id = B.ssd_pcPart_id;