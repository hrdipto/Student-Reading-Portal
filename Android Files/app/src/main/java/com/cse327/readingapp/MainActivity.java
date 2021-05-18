package com.cse327.readingapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button studentBtn;
    private Button teacherBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        studentBtn = (Button) findViewById(R.id.studentBtn);
        teacherBtn = (Button) findViewById(R.id.teacherBtn);

//        studentBtn.setOnClickListener((v) {
//            startActivity(new Intent(MainActivity.this, StudentLogin.class));
//        });

        studentBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, StudentLogin.class));
            }
        });

        teacherBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, TeacherLogin.class));
            }
        });
    }
}
