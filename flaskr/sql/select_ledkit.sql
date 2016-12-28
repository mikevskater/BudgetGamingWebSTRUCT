SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN ledkit AS B 
                        ON A.pcPart_id = B.ledkit_pcPart_id;