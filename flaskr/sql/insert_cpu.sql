INSERT INTO cpu 
        (
         cpu_socket, 
         cpu_cores,
         cpu_threads,
         cpu_frequency,
         cpu_cache,
         cpu_wattage,
         cpu_pcPart_id,
         cpu_pcBuild_id
         ) 
        VALUES (
                ?, 
                ?, 
                ?, 
                ?, 
                ?, 
                ?, 
                ?,
                ?
                )