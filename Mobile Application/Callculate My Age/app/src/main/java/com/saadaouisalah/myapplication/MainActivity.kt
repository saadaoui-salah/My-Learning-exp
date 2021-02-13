package com.saadaouisalah.myapplication

import android.content.ContentValues
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        fun addData(card:String,date:String){
            val values = ContentValues()
            values.put("Card",card)
            values.put("Date",date)
            val db:DbManager = DbManager(this)
            val id = db.insertValues(values)
            if(id>0){
                Toast.makeText(this,"Greet",Toast.LENGTH_LONG)
                print(id)
            }
        }
        btn.setOnClickListener{
            val cards = arrayOf("t1","t2","t2","t3")
            val dates = arrayOf(etd1.text.toString(),etd2.text.toString(),etd3.text.toString(),etd4.text.toString())
            for (i in 0..3){
                addData(cards[i],dates[i])
            }
        }
    }

    }