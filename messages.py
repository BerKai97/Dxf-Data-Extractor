from enum import Enum

class Language(Enum):
    EN = "EN"
    TR = "TR"

class Message(Enum):
    SELECT_CSV_FILE = "SELECT_CSV_FILE"
    SELECT_DXF_FILE = "SELECT_DXF_FILE"
    START = "START"
    STATUS_IDLE = "STATUS_IDLE"
    STATUS_PROCESSING = "STATUS_PROCESSING"
    STATUS_COUNTED = "STATUS_COUNTED"
    STATUS_COMPNOTCOST = "STATUS_COMPNOTCOST"
    STATUS_COMPCOST = "STATUS_COMPCOST"
    STATUS_ERROR = "STATUS_ERROR"
    NOPRICEFILE = "NOPRICEFILE"
    NODXFFILE = "NODXFFILE"
    YES = "YES"
    NO = "NO"

class Messages:
    def __init__(self):
        self.current_language = Language.TR

        self.messages = {
            Language.EN: {
                Message.SELECT_CSV_FILE: 'Select Price CSV File',
                Message.SELECT_DXF_FILE: 'Select DXF File',
                Message.START: 'Start',
                Message.STATUS_IDLE: 'Status: Idle',
                Message.STATUS_PROCESSING: "Status: Processing... Please wait, this may take a while.",
                Message.STATUS_COUNTED: "Status: Assets counted. \n If csv file is selected, calculating cost...",
                Message.STATUS_COMPNOTCOST: "Status: Process completed. \n Cost: Not calculated.",
                Message.STATUS_COMPCOST: "Status: Process completed. \n Cost: ",
                Message.STATUS_ERROR: "Status: Error. \n {}",
                Message.NOPRICEFILE: "No price CSV file selected. Costs won't be calculated. \nContinue?",
                Message.NODXFFILE: 'No DXF file selected.',
                Message.YES: 'Yes',
                Message.NO: 'No',
            },
            
            Language.TR: {
                Message.SELECT_CSV_FILE: 'Fiyat CSV Dosyası Seç',
                Message.SELECT_DXF_FILE: 'DXF Dosyası Seç',
                Message.START: 'Başlat',
                Message.STATUS_IDLE: 'Durum: Boşta',
                Message.STATUS_PROCESSING: "Durum: İşleniyor... Lütfen bekleyin, bu biraz zaman alabilir.",
                Message.STATUS_COUNTED: "Durum: Varlıklar sayıldı. \n Eğer csv dosyası seçilmişse, maliyet hesaplanıyor...",
                Message.STATUS_COMPNOTCOST: "Durum: İşlem tamamlandı. \n Maliyet: Hesaplanmadı.",
                Message.STATUS_COMPCOST: "Durum: İşlem tamamlandı. \n Maliyet: ",
                Message.STATUS_ERROR: "Durum: Hata. \n {}",
                Message.NOPRICEFILE: "Fiyat CSV dosyası seçilmedi. Maliyetler hesaplanmayacak. \nDevam etmek istiyor musunuz?",
                Message.NODXFFILE: 'DXF dosyası seçilmedi.',
                Message.YES: 'Evet',
                Message.NO: 'Hayır',
            }

        }

    def get(self, message):
        return self.messages[self.current_language][message]

    def set_language(self, language):
        for land in Language:
            if land.value == language:
                self.current_language = land
                return