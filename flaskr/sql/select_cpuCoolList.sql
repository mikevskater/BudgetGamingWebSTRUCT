SELECT pcPart_id, pcPart_name, pcPart_modelNumber, pcPart_price
        FROM pcPart AS A 
                JOIN cpuCool AS B 
                        ON A.pcPart_id = B.cpuCool_pcPart_id;