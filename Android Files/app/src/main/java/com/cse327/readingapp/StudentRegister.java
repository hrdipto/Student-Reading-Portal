package com.cse327.readingapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class StudentRegister extends AppCompatActivity {

    private EditText namet;
    private EditText emailt;
    private EditText passt;
    private Button registerBtn;
    private TextView loginText;
    String name, userEmail, userPass;
    String userClass = "student";


    private FirebaseAuth firebaseAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student_register);
        setupUIViews();

        firebaseAuth = FirebaseAuth.getInstance();

        registerBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(validate()) {
                    //write to database
                    String user_email = emailt.getText().toString().trim();
                    String user_password = passt.getText().toString().trim();

                    firebaseAuth.createUserWithEmailAndPassword(user_email, user_password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {

                            if(task.isSuccessful()) {
                                Toast.makeText(StudentRegister.this, "Registration Successful", Toast.LENGTH_SHORT).show();
                                startActivity(new Intent(StudentRegister.this, MainActivity.class));
                            } else {
                                Toast.makeText(StudentRegister.this, "Registration Failed", Toast.LENGTH_SHORT).show();
                            }
                        }
                    });
                }
            }
        });

        loginText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(StudentRegister.this, StudentLogin.class));
            }
        });
    }

    private void setupUIViews() {
        namet = (EditText) findViewById(R.id.namet);
        emailt = (EditText) findViewById(R.id.emailt);
        passt = (EditText) findViewById(R.id.passt);
        registerBtn = (Button) findViewById(R.id.registerBtn);
        loginText = (TextView) findViewById(R.id.loginText);
    }

    private Boolean validate() {
        Boolean result = false;

        name = namet.getText().toString();
        userEmail =  emailt.getText().toString();
        userPass = passt.getText().toString();

        if( name.isEmpty() || userEmail.isEmpty() || userPass.isEmpty() ) {
            Toast.makeText(this, "Please enter all the details", Toast.LENGTH_SHORT).show();
        } else {
            result = true;
        }

        return  result;
    }
}
