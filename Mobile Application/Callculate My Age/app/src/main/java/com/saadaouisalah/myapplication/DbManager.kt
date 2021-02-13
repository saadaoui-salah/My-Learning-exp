package com.saadaouisalah.myapplication

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class DbManager {
    val dbName = "Data"
    val dbTable = "Table"
    val colID = "ID"
    val colCard = "Card"
    val colDate = "Date"
    val dbVersion =1
    val sqlCreate = "CREATE TABLE IF NOT EXISTS "+dbTable+"("+colID+" INTEGER PRIMARY KEY, "+colCard+"TEXT,"+colDate+" TEXT"
    var sql:SQLiteDatabase?=null

    constructor(context: Context){
        val db = DBHelper(context)
        sql = db.writableDatabase

    }
    inner class DBHelper:SQLiteOpenHelper{
        var context:Context?=null
        constructor(context:Context):super(context,dbName,null,dbVersion){
            this.context = context
        }

        override fun onCreate(p0: SQLiteDatabase?) {
            p0!!.execSQL(sqlCreate)
        }

        override fun onUpgrade(p0: SQLiteDatabase?, p1: Int, p2: Int) {
            p0!!.execSQL("Drop table IF EXISTS "+dbTable)
        }
    }
    fun insertValues(values:ContentValues):Long{
        val id = sql!!.insert(dbTable,"",values)
        return id
    }

}
