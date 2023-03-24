import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductChooseComponent } from './product-choose/product-choose.component';
import { CreateUserComponent } from './create-user/create-user.component';
import { MenuComponent } from './menu/menu.component';
import { CheckpointComponent } from './checkpoint/checkpoint.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductChooseComponent,
    CreateUserComponent,
    MenuComponent,
    CheckpointComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule // Add this line
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
