SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN gpu AS B 
                        ON A.pcPart_id = B.gpu_pcPart_id;