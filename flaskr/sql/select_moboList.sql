SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN mobo AS B 
                        ON A.pcPart_id = B.mobo_pcPart_id;