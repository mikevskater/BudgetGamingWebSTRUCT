INSERT INTO psu 
        (
         psu_watt, 
         psu_effiency,
         psu_8pin,
         psu_6pin,
         psu_4pin,
         psu_molex,
         psu_sata,
         psu_floppy,
         psu_pcPart_id,
         psu_pcBuild_id
         ) 
        VALUES (
                ?, 
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
                )