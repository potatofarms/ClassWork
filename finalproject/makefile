FILENAME = count.c
OUT      = count.elf
#FLAGS	 = 
FLAGS	 = -lserial -lconio -lshell

${OUT}: ${FILENAME}
	msp430-gcc -mmcu=msp430g2553 ${FILENAME} -g -o ${OUT} ${FLAGS} 

flash: ${OUT}
	mspdebug rf2500 'prog ${OUT}'

clean:
	rm -rf *.o *.elf *.out

erase:
	mspdebug rf2500 erase

debug: ${OUT}
	(mspdebug rf2500 "gdb" 1>/dev/null &); msp430-gdb ${OUT} -ex "target remote :2000"
