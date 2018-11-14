package com.example.hellboy.handocrfinal;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;

public class Doc extends AppCompatActivity {
    File directory;
    File[] files;
    String[] theNamesOfFiles;
    int i;
    ArrayAdapter<String>   adapter;
    ListView listView;
    String selectedFromList,shareList;
    TextView open;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.doc);
        open=(TextView)findViewById(R.id.tex);
        open.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openpdf();
            }
        });



    }
    public void openpdf() {

        Intent intent = new Intent();
        intent.setAction(android.content.Intent.ACTION_VIEW);
        File file = new File(Environment.getExternalStorageDirectory().getPath()+"/PDF/Name.pdf");
        if (file!=null)
        {
            intent.setDataAndType(Uri.fromFile(file), "application/pdf");
            startActivity(intent);
        }
        else
        {
            Toast.makeText(this,"Missing",Toast.LENGTH_LONG).show();
        }
    }
}
