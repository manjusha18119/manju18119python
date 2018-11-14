package com.example.hellboy.handocrfinal;

import android.Manifest;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.support.annotation.RequiresApi;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.itextpdf.text.BaseColor;
import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Element;
import com.itextpdf.text.Font;
import com.itextpdf.text.PageSize;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfPCell;
import com.itextpdf.text.pdf.PdfPTable;
import com.itextpdf.text.pdf.PdfWriter;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;

public class Final extends AppCompatActivity {
    Button share1;
    TextView txtView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.next2);
        Bundle bundle = getIntent().getExtras();
        String message = null;
        if (bundle != null) {
            message = bundle.getString("message");
        }
        else
        {
            Toast.makeText(Final.this, "null",
                    Toast.LENGTH_LONG).show();
        }

        txtView = (TextView) findViewById(R.id.e1);
        txtView.setText(message);
        share1=(Button)findViewById(R.id.share);
        share1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent sharingIntent = new Intent(android.content.Intent.ACTION_SEND);
                sharingIntent.setType("text/plain");
                String shareBody = txtView.getText().toString();
                sharingIntent.putExtra(android.content.Intent.EXTRA_SUBJECT, "Subject Here");
                sharingIntent.putExtra(android.content.Intent.EXTRA_TEXT, shareBody);
                startActivity(Intent.createChooser(sharingIntent, "Share via"));
            }
        });
        Button exp=(Button)findViewById(R.id.pdf);
        exp.setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.M)
            @Override
            public void onClick(View view) {
                if (checkSelfPermission(android.Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {

                    //File write logic here
                    pdf();
                }
                else {
                    ActivityCompat.requestPermissions(Final.this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 1);
                }
            }
        });
    }
    private void pdf()
    {





        String FILE = Environment.getExternalStorageDirectory().toString()
                + "/PDF/" + "Name.pdf";

        // Add Permission into Manifest.xml
        // <uses-permission
        // android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

        // Create New Blank Document
        Document document = new Document(PageSize.A4);

        // Create Directory in External Storage
        String root = Environment.getExternalStorageDirectory().toString();
        File myDir = new File(root + "/PDF");
        myDir.mkdirs();

        // Create Pdf Writer for Writting into New Created Document
        try {
            PdfWriter.getInstance(document, new FileOutputStream(FILE));

            // Open Document for Writting into document
            document.open();

            // User Define Method
            addMetaData(document);
            addTitlePage(document);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (DocumentException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Close Document after writting all content
        document.close();

        Toast.makeText(this, "PDF File is Created. Location : " + FILE,
                Toast.LENGTH_LONG).show();
    }

    // Set PDF document Properties
    public void addMetaData(Document document)

    {
        document.addTitle("RESUME");
        document.addSubject("Person Info");
        document.addKeywords("Personal,	Education, Skills");
        document.addAuthor("TAG");
        document.addCreator("TAG");
    }

    public void addTitlePage(Document document) throws DocumentException {

        String pdftext=txtView.getText().toString();
        // Font Style for Document
        Font catFont = new Font(Font.FontFamily.TIMES_ROMAN, 18, Font.BOLD);
        Font titleFont = new Font(Font.FontFamily.TIMES_ROMAN, 22, Font.BOLD
                | Font.UNDERLINE, BaseColor.GRAY);
        Font smallBold = new Font(Font.FontFamily.TIMES_ROMAN, 12, Font.BOLD);
        Font normal = new Font(Font.FontFamily.TIMES_ROMAN, 12, Font.NORMAL);

        // Start New Paragraph
        Paragraph prHead = new Paragraph();
        // Set Font in this Paragraph
        prHead.setFont(titleFont);
        // Add item into Paragraph
        prHead.add("RESUME – Name\n");

        // Create Table into Document with 1 Row
        PdfPTable myTable = new PdfPTable(1);
        // 100.0f mean width of table is same as Document size
        myTable.setWidthPercentage(100.0f);

        // Create New Cell into Table
        PdfPCell myCell = new PdfPCell(new Paragraph(""));

        Paragraph prPersinalInfo = new Paragraph();
        prPersinalInfo.setFont(smallBold);
        prPersinalInfo.add(pdftext);

        prPersinalInfo.setAlignment(Element.ALIGN_CENTER);

        document.add(prPersinalInfo);
        document.add(myTable);

        document.add(myTable);

        Paragraph prProfile = new Paragraph();
        prProfile.setFont(smallBold);

        document.add(prProfile);

        // Create new Page in PDF
        document.newPage();
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if(grantResults[0]== PackageManager.PERMISSION_GRANTED){
           // Log.v(TAG,"Permission: "+permissions[0]+ "was "+grantResults[0]);
            //resume tasks needing this permission
            AlertDialog alertDialog = new AlertDialog.Builder(Final.this).create();
            alertDialog.setTitle("Thank you");
            alertDialog.setMessage("permission granted");
            alertDialog.setButton(AlertDialog.BUTTON_NEUTRAL, "OK",
                    new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.dismiss();
                        }
                    });
            alertDialog.show();
        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        if (id == R.id.doc) {
            // return true;
            /**  String url = "http://www.kasoftsol.in";
             Intent i = new Intent(Intent.ACTION_VIEW);
             i.setData(Uri.parse(url));
             startActivity(i);**/
            Intent intent = new Intent(Final.this, Doc.class);
            startActivity(intent);

        }

        return super.onOptionsItemSelected(item);
    }
    }

