#include <map>
#include <string>
#include <iostream>

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "myhead.h"

#include "cJSON.h"
#include "cJSON_Utils.h"

struct MmapRecord{
    char *addr;
    int fd;
    struct stat sb;
    public:
        MmapRecord(){
            printf("record\n");
        };
        template<typename Record>
        MmapRecord(Record&&record){
            printf("MmapRecord copy\n");
        };
};

std::map<std::string,MmapRecord> MmapRecordMap;

#define handle_error(msg) \
    do { perror(msg); exit(EXIT_FAILURE); } while (0)

void mmapWithRecord(char *file){
    MmapRecord record;
    record.fd = open(file, O_RDONLY);
    if (record.fd == -1)
        handle_error("open");

    if (fstat(record.fd, &(record.sb)) == -1)           /* To obtain file size */
        handle_error("fstat");
    record.addr = (char*)mmap(NULL, record.sb.st_size, PROT_READ,
                MAP_PRIVATE, record.fd, 0);
    if (record.addr == MAP_FAILED)
        handle_error("mmap");
    MmapRecordMap[file]=record;
}
void freeMmapWithRecord(char *file){
    MmapRecord *record=&MmapRecordMap[file];
    munmap(record->addr, record->sb.st_size);
    close(record->fd);
}

cJSON *readjson(char *file){
    cJSON *json;
    mmapWithRecord(file);
    json = cJSON_ParseWithLength(MmapRecordMap[file].addr, MmapRecordMap[file].sb.st_size);
    freeMmapWithRecord(file);
    return json;
}




int
mmapexample(int argc, char *argv[])
{
    char *addr;
    int fd;
    struct stat sb;
    off_t offset, pa_offset;
    size_t length;
    ssize_t s;

    if (argc < 3 || argc > 4) {
        fprintf(stderr, "%s file offset [length]\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    fd = open(argv[1], O_RDONLY);
    if (fd == -1)
        handle_error("open");

    if (fstat(fd, &sb) == -1)           /* To obtain file size */
        handle_error("fstat");

    offset = atoi(argv[2]);
    pa_offset = offset & ~(sysconf(_SC_PAGE_SIZE) - 1);
        /* offset for mmap() must be page aligned */

    if (offset >= sb.st_size) {
        fprintf(stderr, "offset is past end of file\n");
        exit(EXIT_FAILURE);
    }

    if (argc == 4) {
        length = atoi(argv[3]);
        if (offset + length > sb.st_size)
            length = sb.st_size - offset;
                /* Can't display bytes past end of file */

    } else {    /* No length arg ==> display to end of file */
        length = sb.st_size - offset;
    }
    //g++指针必须强制转换
    addr = (char*)mmap(NULL, length + offset - pa_offset, PROT_READ,
                MAP_PRIVATE, fd, pa_offset);
    if (addr == MAP_FAILED)
        handle_error("mmap");

    s = write(STDOUT_FILENO, addr + offset - pa_offset, length);
    if (s != length) {
        if (s == -1)
            handle_error("write");

        fprintf(stderr, "partial write");
        exit(EXIT_FAILURE);
    }

    munmap(addr, length + offset - pa_offset);
    close(fd);

    exit(EXIT_SUCCESS);
}
