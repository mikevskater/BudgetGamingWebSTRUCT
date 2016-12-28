SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN hdd AS B 
                        ON A.pcPart_id = B.hdd_pcPart_id;