from django.contrib.auth.models import User
from rest_framework import serializers

class  RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={'password':
        {'write_only':True}}
    
    def save(self):
        p1=self.validated_data['password']
        p2=self.validated_data['password2']
        email=self.validated_data['email']
        if(p1!=p2):
            raise serializers.ValidationError(' Both passwords must be same')
        elif(User.objects.filter(email=email).exists()):
            raise serializers.ValidationError("{'error':'Email already exists'}")
        else:
            account=User(username=self.validated_data['username'],email=email)
            account.set_password(p1)
            account.save()
            return account

        