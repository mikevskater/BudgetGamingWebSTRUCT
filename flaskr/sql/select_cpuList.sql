SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN cpu AS B 
                        ON A.pcPart_id = B.cpu_pcPart_id;