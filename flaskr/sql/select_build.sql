SELECT *
        FROM pcBuild AS A 
                JOIN pcPart AS B 
                        ON A.pcBuild_id = B.pcPart_pcBuild_id;