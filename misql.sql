drop database security_2;

create database security_2;

use security_2;

create Table banco (
  id_banco int primary key auto_increment,
  nombre_banco varchar(255) unique not null,
  codigo_bancario int(4) unique  not null
);


create TABLE usuario (
  id int primary key AUTO_INCREMENT,
  nombre varchar(50) unique not null, 
  password_hash varchar(255),
  rol enum("cliente", "administrador", "soporte") default "cliente"
);



create TABLE cuenta (
  id_cuenta int primary key auto_increment,
  tipo_cuenta enum('corriente','ahorro'),
  numero_cuenta varchar(50) unique not null,
  saldo double(15,2) default 0.00,
  fecha_apertura datetime not null, 
  usuario_id int,
  banco_id int,

  foreign key(usuario_id) references usuario(id),
  foreign key(banco_id) references banco(id_banco)

);


create TABLE data_user (
  id_data int primary key auto_increment,
  nombre varchar(50) not null,
  apellido varchar(50) not null,
  cedula varchar(13)   unique not null,
  telefono varchar(25) unique not null,
  correo varchar(255) unique not null,
  usuario_id int,

  foreign key(usuario_id) references usuario(id)
); 


create TABLE dispositivo (
  id_dispositivo int primary key auto_increment,
  tipo_dispositivo varchar(25),
  marchar varchar(50) not null,
  modelo varchar(50)  not null,
  user_id int,

  foreign key(user_id) references usuario(id)
);

create TABLE tarjeta (
  id_tarjeta int primary key auto_increment,
  numero_tajeta_token varchar(255) not null,
  fecha_vencimiento date, 
  cuenta_id int,
  
  foreign key(cuenta_id) references cuenta(id_cuenta)
);




create TABLE transaccion (
  id int primary key auto_increment,
  tipo_transaccion varchar(25),
  fecha_hora datetime not null,
  monto double(15,2),  
  cuenta_id int, 
  dispositivo_id int,

   foreign key(dispositivo_id) references dispositivo(id_dispositivo),
   
   foreign key(cuenta_id) references cuenta(id_cuenta)
);


create TABLE detalle_transaccion (
  id_detalle int primary key auto_increment,
  descripcion text,
  monto double(15,2), 
  transaccion_id int,

  foreign key(transaccion_id) references transaccion(id)

);