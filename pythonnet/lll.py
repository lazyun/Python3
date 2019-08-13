import clr
clr.AddReference('System.Data')
from System.Data import SqlClient
from System.Data import *
from System.Data import DataTable

import clr
clr.AddReference('System')
# from System import *
clr.AddReference('System.Memory')
from System import Console
from System import Data

sqlConnectionString = "<sql-connection-string>"
sqlDbConnection = SqlClient.SqlConnection(sqlConnectionString)
sqlDbConnection.Open()

workTable = DataTable()
workTable.Columns.Add("Col1", Byte)
workTable.Columns.Add("Col2",Byte)
workTable.Columns.Add("Col3", Int32)
workTable.Columns.Add("Col4", Byte)
workTable.Columns.Add("Col5", Byte)
workTable.Columns.Add("Col6", Single)

sampleArray = [Byte(7), Byte(8), Int32(1), Byte(15), Byte(12), Single(0.34324)]
for i in range (0, 189000) :
    workTable.Rows.Add(Array[object](sampleArray))

cmd = SqlClient.SqlCommand("truncate table dbo.MyTable", sqlDbConnection);
def bulkLoadEsgData ():
    sbc = SqlClient.SqlBulkCopy(sqlConnectionString, SqlClient.SqlBulkCopyOptions.TableLock, BulkCopyTimeout=0, DestinationTableName="dbo.MyTable")
    sbc.WriteToServer(workTable)

# Start simulation
Console.WriteLine("Enter number of simulations (1 simulation = 189,000 data rows):"+"\n")
strN = Console.ReadLine()

n = int(strN)
cmd.ExecuteNonQuery()
for i in range (0, n):
    bulkLoadEsgData()

sqlDbConnection.Close()
Environment.Exit(1111)