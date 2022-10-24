-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_conversor
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `db_conversor` ;

-- -----------------------------------------------------
-- Schema db_conversor
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_conversor` DEFAULT CHARACTER SET utf8 ;
USE `db_conversor` ;

-- -----------------------------------------------------
-- Table `db_conversor`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_conversor`.`usuarios` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_conversor`.`audios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_conversor`.`audios` (
  `id_conversion` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `audio` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id_conversion`),
  INDEX `fk_conversiones_usuarios_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_conversiones_usuarios`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `db_conversor`.`usuarios` (`id_usuario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_conversor`.`textos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_conversor`.`textos` (
  `id_textos` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `texto` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id_textos`),
  INDEX `fk_textos_usuarios1_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_textos_usuarios1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `db_conversor`.`usuarios` (`id_usuario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
