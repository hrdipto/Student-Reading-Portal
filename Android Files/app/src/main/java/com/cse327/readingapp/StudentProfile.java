package com.cse327.readingapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;


public class StudentProfile extends AppCompatActivity {

    private FirebaseAuth firebaseAuth;
    private Button logoutBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student_profile);

        firebaseAuth = FirebaseAuth.getInstance();

        logoutBtn = (Button) findViewById(R.id.logoutBtn);

        logoutBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                firebaseAuth.signOut();
                finish();
                Toast.makeText(StudentProfile.this, "Logout Successful", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(StudentProfile.this, MainActivity.class));
            }
        });
    }
}
