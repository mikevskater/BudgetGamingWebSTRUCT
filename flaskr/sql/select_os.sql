SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN os AS B 
                        ON A.pcPart_id = B.os_pcPart_id;