package com.example.hellboy.handocrfinal;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Next extends AppCompatActivity {

    int i=0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.next);



        Bundle bundle = getIntent().getExtras();
        String message = null;
        if (bundle != null) {
            message = bundle.getString("message");
        }
        else
        {
            Toast.makeText(Next.this, "null",
                Toast.LENGTH_LONG).show();
        }

        final EditText txtView = (EditText) findViewById(R.id.e1);
        txtView.setText(message);



        txtView.setFocusableInTouchMode(true);




        Button button1=(Button)findViewById(R.id.b1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent in =new Intent(Next.this,MainActivity.class);
                startActivity(in);
                finish();





            }
        });




        Button button=(Button)findViewById(R.id.next);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String msg=txtView.getText().toString();
                Intent intent=new Intent(Next.this,Final.class);
                intent.putExtra("message",msg);
                startActivity(intent);
            }
        });
    }

}
