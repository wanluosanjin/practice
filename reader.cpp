#include <map>
#include <unordered_map>
#include <deque>
#include <string>
#include <iostream>

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <ctype.h>
#include <float.h>


struct MmapRecord{
    char *addr;
    int fd;
    struct stat sb;
};

static std::map<std::string,MmapRecord> MmapRecordMap;

#define handle_error(msg) \
    do { perror(msg); exit(EXIT_FAILURE); } while (0)

static void mmapWithRecord(const char *file){
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

static void freeMmapWithRecord(const char *file){
    MmapRecord *record=&MmapRecordMap[file];
    munmap(record->addr, record->sb.st_size);
    close(record->fd);
}

#define name_void 0
#define name_obj 1
#define name_str 2
#define name_func 3
#define name_num32 4
#define name_num64 5
#define name_double 6

struct Name{
    char* name;
    size_t len;
    size_t type;
    void* to;
};

struct Object{
    void* pstart;
    size_t len;
    size_t type;
    struct Name* name;
    struct Object* next;
    struct Object* father;
}

struct BufferCater{
    void* pstart;
    size_t len;

    struct BufferCater* next;
}

static std::deque<Buffer> bufDeque;

static std::deque<size_t> objDeque;

static std::deque<size_t> funcDeque;

static std::unordered_map<std::string,Name> nameMap;

static size_t pstart;
static size_t pend;
static size_t pnow;

static int nameing;
static int buffering;

#define isname 2
#define isstringing 2
#define isstringing 2
inline void notname(){

}
inline int stringReady(){
    pstart=pnow+1;
}
inline void word(){
    word = 1;
}

/*
          2 3 4 5 6 7       30 40 50 60 70 80 90 100 110 120
        -------------      ---------------------------------
       0:   0 @ P ` p     0:    (  2  <  F  P  Z  d   n   x
       1: ! 1 A Q a q     1:    )  3  =  G  Q  [  e   o   y
       2: " 2 B R b r     2:    *  4  >  H  R  \  f   p   z
       3: # 3 C S c s     3: !  +  5  ?  I  S  ]  g   q   {
       4: $ 4 D T d t     4: "  ,  6  @  J  T  ^  h   r   |
       5: % 5 E U e u     5: #  -  7  A  K  U  _  i   s   }
       6: & 6 F V f v     6: $  .  8  B  L  V  `  j   t   ~
       7: ' 7 G W g w     7: %  /  9  C  M  W  a  k   u  DEL
       8: ( 8 H X h x     8: &  0  :  D  N  X  b  l   v
       9: ) 9 I Y i y     9: '  1  ;  E  O  Y  c  m   w
       A: * : J Z j z
       B: + ; K [ k {
       C: , < L \ l |
       D: - = M ] m }
       E: . > N ^ n ~
       F: / ? O _ o DEL
*/
//a fuking stupid jump table
static size_t _to[256]

//\n and \r and ;
static void _to10and13and59(){

}
//space and \t
static void _to32and9(){

}
//" and '
static void _to34and39(){

}
//(
static void _to40(){

}
//)
static void _to41(){

}
//,
static void _to44(){

}
//.
static void _to46(){

}
//0
static void _to48(){

}
//1_9
static void _to49_57(){

}
//=
static void _to61(){

}
//A_Z and _ and a_z
static void _to65_90and_and97_122(){
    word();
}
//[
static void _to91(){

}
//]
static void _to93(){

}
//{
static void _to123(){

}
//}
static void _to125(){

}

Name * readfile(const char *file){
    mmapWithRecord(file);
}
