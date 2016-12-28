SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN ram AS B 
                        ON A.pcPart_id = B.ram_pcPart_id;