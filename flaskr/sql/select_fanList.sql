SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN fan AS B 
                        ON A.pcPart_id = B.fan_pcPart_id;